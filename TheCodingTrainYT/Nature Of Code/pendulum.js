class Pendulum {
  constructor(x, y, r) {
    this.origin = createVector(x, y);
    this.position = createVector();
    this.r = r;
    this.angle = PI / 4;

    this.aVelocity = 0.0;
    this.aAcceleration = 0.0;
    this.damping = 0.995; // 0.995;
    this.ballr = 48.0;
  }

  update() {
    let gravity = 0.4;
    this.aAcceleration = ((-1 * gravity) / this.r) * sin(this.angle);
    this.aVelocity += this.aAcceleration;
    this.aVelocity *= this.damping // arbitrary damping
    this.angle += this.aVelocity;
  }

  show() {
    this.position.set(this.r * sin(this.angle), this.r * cos(this.angle), 0);
    this.position.add(this.origin);

    stroke(255);
    strokeWeight(2);

    // the pendulum's arm
    line(this.origin.x, this.origin.y, this.position.x, this.position.y);

    ellipseMode(CENTER);
    fill(127);

    // the pendulum's bob
    ellipse(this.position.x, this.position.y, this.ballr, this.ballr);
  }
}
