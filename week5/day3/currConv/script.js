const apiKey = '48d0abf33ece82fc0dcc8106';  // Replace with your actual API key
const baseUrl = `https://v6.exchangerate-api.com/v6/${apiKey}`;

const fromSelect = document.getElementById('from-currency');
const toSelect = document.getElementById('to-currency');
const amountInput = document.getElementById('amount');
const convertBtn = document.getElementById('convert-btn');
const switchBtn = document.getElementById('switch-btn');
const resultDiv = document.getElementById('result');

async function fetchCurrencies() {
  try {
    const res = await fetch(`${baseUrl}/codes`);
    const data = await res.json();
    if (data.result === 'success') {
      return data.supported_codes; // array of [code, name]
    } else {
      throw new Error('Could not fetch currencies');
    }
  } catch (error) {
    alert('Error fetching currencies: ' + error.message);
    return [];
  }
}

function populateDropdowns(currencies) {
  currencies.forEach(([code, name]) => {
    const optionFrom = document.createElement('option');
    optionFrom.value = code;
    optionFrom.textContent = `${code} - ${name}`;
    fromSelect.appendChild(optionFrom);

    const optionTo = document.createElement('option');
    optionTo.value = code;
    optionTo.textContent = `${code} - ${name}`;
    toSelect.appendChild(optionTo);
  });

  // Set some defaults
  fromSelect.value = 'USD';
  toSelect.value = 'EUR';
}

async function convertCurrency(from, to, amount) {
  try {
    const res = await fetch(`${baseUrl}/pair/${from}/${to}/${amount}`);
    const data = await res.json();
    if (data.result === 'success') {
      return data.conversion_result;
    } else {
      throw new Error('Conversion failed');
    }
  } catch (error) {
    alert('Error during conversion: ' + error.message);
    return null;
  }
}

async function handleConversion() {
  const from = fromSelect.value;
  const to = toSelect.value;
  const amount = parseFloat(amountInput.value);

  if (isNaN(amount) || amount <= 0) {
    alert('Please enter a valid amount');
    return;
  }

  resultDiv.textContent = 'Converting...';

  const converted = await convertCurrency(from, to, amount);

  if (converted !== null) {
    resultDiv.textContent = `${amount} ${from} = ${converted.toFixed(2)} ${to}`;
  } else {
    resultDiv.textContent = '';
  }
}

function switchCurrencies() {
  const temp = fromSelect.value;
  fromSelect.value = toSelect.value;
  toSelect.value = temp;

  // Recalculate conversion
  handleConversion();
}

// Event listeners
convertBtn.addEventListener('click', handleConversion);
switchBtn.addEventListener('click', switchCurrencies);

// Initialize app
fetchCurrencies()
  .then(populateDropdowns)
  .catch(err => console.error(err));
