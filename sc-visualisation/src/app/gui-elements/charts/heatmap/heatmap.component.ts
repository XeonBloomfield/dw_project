import { Component, OnInit } from '@angular/core';
import * as d3 from 'd3';

@Component({
  selector: 'app-heatmap',
  templateUrl: './heatmap.component.html',
  styleUrls: ['./heatmap.component.scss']
})

export class HeatmapComponent implements OnInit {
  private svg!: any;
  private margin = 50;
  private width = 750 - (this.margin * 2);
  private height = 400 - (this.margin * 2);
  private n = 256;
  private m = 256;
  private values = new Array(this.n * this.m);
  constructor() { }

  ngOnInit(): void {
    this.createSvg();
    this.drawHeatmap();
    for (var j = 0.5, k = 0; j < this.m; ++j) {
      for (var i = 0.5; i < this.n; ++i, ++k) {
        this.values[k] = this.goldsteinPrice(i / this.n * 4 - 2, 1 - j / this.m * 3);
    }
}

  }

  private goldsteinPrice(x: number, y: number) {
    return (1 + Math.pow(x + y + 1, 2) * (19 - 14 * x + 3 * x * x - 14 * y + 6 * x * x + 3 * y * y))
    * (30 + Math.pow(2 * x - 3 * y, 2) * (18 - 32 * x + 12 * x * x + 48 * y - 36 * x * y + 27 * y * y));
  }

  private createSvg(): void {
    this.svg = d3.select("figure#heatmap")
    .append("svg")
    .attr("width", this.width + (this.margin * 2))
    .attr("height", this.height + (this.margin * 2))
    .append("g")
    .attr("transform", "translate(" + this.margin + "," + this.margin + ")");
  }

  private drawHeatmap(): void {
    const x = d3.scaleLinear()
    .domain([0, 256])
    .range([ 0, this.width ]);

    this.svg.append("g")
      .attr("transform", "translate(0," + this.height + ")")
      .call(d3.axisBottom(x))

    const y = d3.scaleLinear()
    .domain([0, 256])
    .range([ this.height, 0 ]);
    this.svg.append("g")
    .call(d3.axisLeft(y));


    var color = d3.scaleLinear<string>()
      .domain([0, this.values.length])
      .range(["transparent",  "#69b3a2"])

    console.log(this.values)
/*
    var densityData = d3.contourDensity()
    .x(function(d) { return x(d[0]); })
    .y(function(d) { return y(d[1]); })
    .size([this.width, this.height])
    .bandwidth(20)
    (this.values)
*/

    var densityData = d3.contourDensity()
    .size([this.n, this.m])
    .thresholds(Array.from({ length: 19 }, (_, i) => Math.pow(2, i + 2)))
    (this.values);
    console.log(densityData)


    this.svg.append("path")
    .attr("class", "density")
    .enter().append("path")
    .attr("d", d3.geoPath())
    .data(densityData)
    .attr("fill", function(d: { value: d3.NumberValue; }) { return color(d.value); })

  }

}
