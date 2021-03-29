var x = 0;

function setup() {
  createCanvas(600, 400);
}

function draw() {
  background(0);

  stroke(255);
  strokeWeight(4);
  noFill();

  if (mouseX > 300) {
    ellipse(300, 200, 100, 100);
  } else {
    rectMode(CENTER);
    rect(300, 200, 100, 100);
  }
}
