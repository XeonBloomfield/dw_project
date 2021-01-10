export class Square {
  constructor(private ctx: CanvasRenderingContext2D | null | undefined) {}

  draw(x: number, y: number, z: number) {
    if (this.ctx) {
      this.ctx.fillRect(z * x, z * y, z, z);
    }
  }

  move(y: number, z: number) {
    if (this.ctx) {
      const max = this.ctx.canvas.width / z;
      const canvas = this.ctx.canvas;
      let x = 0;
      const i = setInterval(() => {
        if (this.ctx) {
        this.ctx.clearRect(0, 0, canvas.width, canvas.height);
        this.draw(x, y, z);
        x++;
        if (x >= max) {
          clearInterval(i);
        }}
      }, 20);
    }
  }

  erase(){
    if (this.ctx) {
    const canvas = this.ctx.canvas;
      this.ctx.clearRect(0, 0, canvas.width, canvas.height);
    }
  }

}
