class Video {
  constructor(title, uploader, time) {
    this.title = title;
    this.uploader = uploader;
    this.time = time;
  }

  watch() {
    console.log(`${this.uploader} watched all ${this.time} seconds of "${this.title}"!`);
  }
}

const video1 = new Video("Learn JavaScript", "Alice", 300);
video1.watch();

const video2 = new Video("CSS Crash Course", "Bob", 420);
video2.watch();

const videosData = [
  { title: "test1", uploader: "uplod1", time: 600 },
  { title: "test2", uploader: "uplod2", time: 800 },
  { title: "test3", uploader: "uplod3", time: 750 },
  { title: "test4", uploader: "uplod4", time: 120 },
  { title: "test5", uploader: "uplod1", time: 540 },
];

const videoInstances = [];

videosData.forEach(data => {
  const video = new Video(data.title, data.uploader, data.time);
  video.watch();
  videoInstances.push(video);
});
