var circle1 = {
  x: 0,
  y: 200,
  diameter: 50
};

var circle2 = {
  x: 10,
  y: 210,
  diameter: 60
}

var color = {
  r: 218,
  g: 160,
  b: 221
};

function setup() {
  createCanvas(600, 400);
}

function draw() {
  background(color.r, color.g, color.b);

  fill(250, 200, 200);
  ellipse(circle1.x, circle1.y, circle1.diameter, circle1.diameter);

  fill(150, 100, 100);
  ellipse(circle2.x, circle2.y, circle2.diameter, circle2.diameter);

  circle1.x += 5;
  circle1.diameter++;

  circle2.x += 5;
  circle2.diameter++;  
}
