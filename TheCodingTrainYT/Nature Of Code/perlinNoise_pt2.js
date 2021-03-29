// var x_offset1 = 0;
// var x_offset2 = 10000;
var inc = 0.01;
var start = 0;

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(51);
  // var x = random(width);

  // var x = map(noise(x_offset1), 0, 1, 0, width);
  // var y = map(noise(x_offset2), 0, 1, 0, height);
  //
  // x_offset1 += 0.02;
  // x_offset2 += 0.02;

  stroke(255);
  noFill();
  beginShape();

  var x_offset = start;
  for (var x = 0; x < width; x++) {
    stroke(255);
    // var y = random(height);
    // var y = noise(x_offset) * height;

    var n = map(noise(x_offset), 0, 1, -50, 50);
    var s = map(sin(x_offset), -1, 1, 0, height);
    var y = s + n;

    vertex(x, y);
    x_offset += inc;
  }

  endShape();
  start += inc;
  // noLoop();
  // ellipse(x, y, 24, 24);
}
