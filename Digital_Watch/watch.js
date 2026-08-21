const currentTime = () => {
  let cutTime = new Date().toLocaleTimeString();
  document.getElementById("clock").innerText = cutTime;
};
currentTime();
setInterval(() => {
  currentTime();
}, 1000);
