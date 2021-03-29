var x_offset = 0;

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(51);
  // var x = random(width);
  var x = map(noise(x_offset), 0, 1, 0, width);
  x_offset += 0.01;
  ellipse(x, 200, 24, 24);
}
