import { Component, ElementRef, Input, OnInit, ViewChild } from '@angular/core';
import * as d3 from "d3";
import { BehaviorSubject } from 'rxjs';
import { GameObject } from 'src/app/wrappers/game-object';

interface Dictionary<T> {
  [Key: string]: T;
}


@Component({
  selector: 'app-line-chart',
  templateUrl: './line-chart.component.html',
  styleUrls: ['./line-chart.component.scss']
})
export class LineChartComponent implements OnInit {
  @ViewChild("chart", { static: true }) protected chartContainer!: ElementRef;
  @Input() dataSubject: BehaviorSubject<GameObject[] | null> = new BehaviorSubject<GameObject[] | null>(null);
  private svg!: any;
  private margin = 50;
  private width = 750 - (this.margin * 2);
  private height = 400 - (this.margin * 2);
  private currentDict: Dictionary<[Dictionary<number>]> = {};
  private colours = ["red", "blue", "orange", "purple"]
  private player2Colour: Dictionary<string> = {};
  private datalen = 0;
  private datahaj = 200;

  constructor() { }

  ngOnInit(): void {
    this.createSvg();

    this.dataSubject.subscribe( data => {
      this.drawBars(data);
    })
  }

  private createSvg(): void {
    this.svg = d3.select("figure#line")
    .append("svg")
    .attr("width", this.width + (this.margin * 2))
    .attr("height", this.height + (this.margin * 2))
    .append("g")
    .attr("transform", "translate(" + this.margin + "," + this.margin + ")");
  }

  private drawBars(data: GameObject[] | null): void {
    // Create the X-axis band scale
    if (data) {
      this.svg.selectAll("g").remove()
      const x = d3.scaleLinear()
      .range([0, this.width])
      .domain([0, this.datalen])

      // Draw the X-axis on the DOM
      this.svg.append("g")
      .attr("transform", "translate(0," + this.height + ")")
      .call(d3.axisBottom(x));

      // Create the Y-axis band scale
      // todo get change of
      const y = d3.scaleLinear()
      .domain([0, this.datahaj+this.datahaj*0.2])
      .range([this.height, 0]);

      // Draw the Y-axis on the DOM
      this.svg.append("g")
      .call(d3.axisLeft(y));

      // Line for each player
      this.svg.selectAll("path").remove()

      for(var i = 0; i < data.length; i++ ) {
        if (data[i]['name'] in this.currentDict){
          this.currentDict[data[i]['name']].push({x: this.currentDict[data[i]['name']].length, y: data[i].unitResValue});
        }
        else {
          this.player2Colour[data[i]['name']] = this.colours[Object.keys(this.currentDict).length];
          this.currentDict[data[i]['name']] = [{x: 0, y: data[i].unitResValue}]
        }
        this.datalen = Math.max(this.datalen, this.currentDict[data[i]['name']].length)
        this.datahaj = Math.max(this.datahaj, data[i].unitResValue)
      }
      this.svg.selectAll("path").remove()
      for (let player in this.currentDict){

        const line = d3
        .line()
        .x(d => d[0])
        .y(d => d[1])
        .curve(d3.curveMonotoneX);
        const points: [number, number][] = this.currentDict[player].map(
          d => [x(d.x), y(d.y)]
        );
        this.svg.append("path")
        .attr("class", "line")
        .attr("d", line(points)) // use the return value of slice(xy) as the data, 'd'
        .style("fill", "none")
        .style("stroke", this.player2Colour[player])
        .style("stroke-width", 2);
      }
    }
  }
}
