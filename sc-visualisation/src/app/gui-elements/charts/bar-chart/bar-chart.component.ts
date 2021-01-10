import { Component, Input, OnInit } from '@angular/core';
import * as d3 from 'd3';
import { BehaviorSubject } from 'rxjs';
import { GameObject } from 'src/app/wrappers/game-object';

@Component({
  selector: 'app-bar-chart',
  templateUrl: './bar-chart.component.html',
  styleUrls: ['./bar-chart.component.scss']
})
export class BarChartComponent implements OnInit {

  @Input() dataSubject: BehaviorSubject<GameObject[] | null> = new BehaviorSubject<GameObject[] | null>(null);
  private svg!: any;
  private margin = 50;
  private width = 750 - (this.margin * 2);
  private height = 400 - (this.margin * 2);
  constructor() { }

  ngOnInit(): void {
    this.createSvg();

    this.dataSubject.subscribe( data => {
      this.drawBars(data);
    })
  }

  private createSvg(): void {
    this.svg = d3.select("figure#bar")
    .append("svg")
    .attr("width", this.width + (this.margin * 2))
    .attr("height", this.height + (this.margin * 2))
    .append("g")
    .attr("transform", "translate(" + this.margin + "," + this.margin + ")");
  }

  private drawBars(data: GameObject[] | null): void {
    // Create the X-axis band scale
    if (data) {
      const x = d3.scaleBand()
      .range([0, this.width])
      .domain(data.map(d => d.name))
      .padding(0.2);

      // Draw the X-axis on the DOM
      this.svg.append("g")
      .attr("transform", "translate(0," + this.height + ")")
      .call(d3.axisBottom(x))
      .selectAll("text")
      .attr("transform", "translate(-10,0)rotate(-45)")
      .style("text-anchor", "end");

      // Create the Y-axis band scale
      const y = d3.scaleLinear()
      .domain([0, 300])
      .range([this.height, 0]);

      // Draw the Y-axis on the DOM
      this.svg.append("g")
      .call(d3.axisLeft(y));

      // Create and fill the bars
      this.svg.selectAll("rect").remove()
      this.svg.selectAll("bars")
      .data(data)
      .enter()
      .append("rect")
      .attr("x", (d: { name: string; }) => x(d.name))
      .attr("y", (d: { unitResValue: d3.NumberValue; }) => y(d.unitResValue))
      .attr("width", x.bandwidth())
      .attr("height", (d: { unitResValue: d3.NumberValue; }) => this.height - y(d.unitResValue))
      .attr("fill", "#d04a35");

    }
  }
}
