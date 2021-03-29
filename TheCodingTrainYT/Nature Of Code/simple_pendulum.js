let pendul;

function setup() {
  createCanvas(640, 360);

  // make a Pendulum object
  pendul = new Pendulum(width / 2, 0, 175);
}

function draw() {
  background(0);
  pendul.update();
  pendul.show();
}
