import requests
import psycopg2
import random
from typing import List, Dict, Optional
from contextlib import contextmanager
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database configuration
DB_CONFIG = {
    'dbname': 'bootcamp',
    'user': 'postgres',
    'password': '123',
    'host': 'localhost',
    'port': '5432'
}

API_URL = 'https://restcountries.com/v3.1/all?fields=name,capital,flag,subregion,population'
SAMPLE_SIZE = 10


@contextmanager
def db_connection(db_config: Dict[str, str]):
    """Context manager for database connection handling."""
    conn = None
    try:
        conn = psycopg2.connect(**db_config)
        yield conn
    except psycopg2.Error as e:
        logger.error(f"Database connection error: {e}")
        raise
    finally:
        if conn:
            conn.close()


def create_countries_table(conn) -> None:
    """Create the countries table if it doesn't exist."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS countries (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        capital TEXT NOT NULL,
        flag TEXT NOT NULL,
        subregion TEXT NOT NULL,
        population INTEGER NOT NULL
    );
    """
    try:
        with conn.cursor() as cursor:
            cursor.execute(create_table_query)
            conn.commit()
        logger.info("Countries table created/verified")
    except psycopg2.Error as e:
        logger.error(f"Error creating table: {e}")
        conn.rollback()
        raise


def insert_country_data(conn, country_data: Dict[str, str]) -> None:
    """Insert a single country's data into the database."""
    insert_query = """
    INSERT INTO countries (name, capital, flag, subregion, population)
    VALUES (%s, %s, %s, %s, %s)
    """
    try:
        with conn.cursor() as cursor:
            cursor.execute(insert_query, (
                country_data['name'],
                country_data['capital'],
                country_data['flag'],
                country_data['subregion'],
                country_data['population']
            ))
            conn.commit()
    except psycopg2.Error as e:
        logger.error(f"Error inserting country {country_data.get('name')}: {e}")
        conn.rollback()
        raise


def fetch_countries_data(api_url: str, sample_size: int) -> List[Dict[str, str]]:
    """Fetch countries data from API and return a random sample."""
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        countries = response.json()
        return random.sample(countries, min(sample_size, len(countries)))
    except requests.RequestException as e:
        logger.error(f"API request failed: {e}")
        raise
    except ValueError as e:
        logger.error(f"JSON decoding failed: {e}")
        raise


def process_country_data(raw_country: Dict) -> Optional[Dict[str, str]]:
    """Process raw country data into our required format."""
    try:
        return {
            'name': raw_country['name']['common'],
            'capital': raw_country['capital'][0] if raw_country.get('capital') else 'N/A',
            'flag': raw_country['flag'],
            'subregion': raw_country.get('subregion', 'N/A'),
            'population': raw_country['population']
        }
    except KeyError as e:
        logger.warning(f"Missing expected field in country data: {e}")
        return None


def main() -> None:
    """Main execution function."""
    try:
        # Fetch and process countries data
        raw_countries = fetch_countries_data(API_URL, SAMPLE_SIZE)
        processed_countries = [
            country for country in (
                process_country_data(c) for c in raw_countries
            ) if country is not None
        ]

        # Database operations
        with db_connection(DB_CONFIG) as conn:
            create_countries_table(conn)
            
            for country in processed_countries:
                insert_country_data(conn, country)
            
            logger.info(f"Successfully inserted {len(processed_countries)} countries")

    except Exception as e:
        logger.error(f"Application failed: {e}")
        raise


if __name__ == '__main__':
    main()