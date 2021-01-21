import { Component, OnInit } from '@angular/core';
import { multi } from '../../../../assets/data/data';

@Component({
  selector: 'app-ngx-heatmap',
  templateUrl: './ngx-heatmap.component.html',
  styleUrls: ['./ngx-heatmap.component.scss']
})
export class NgxHeatmapComponent implements OnInit {
  data!: any[];
  width = 562;
  height = 630;
  view: [number, number] = [this.width , this.height];
  legend: boolean = false;
  showLabels: boolean = false;
  animations: boolean = true;
  xAxis: boolean = false;
  yAxis: boolean = false;
  showYAxisLabel: boolean = false;
  showXAxisLabel: boolean = false;

  colorScheme = {
    domain: ['#5AA454', '#E44D25', '#CFC0BB', '#7aa3e5', '#a8385d', '#aae3f5']
  };
  constructor() {
    this.data = this.generateMockData()
    let wut = this.data;
    Object.assign(this, {
      wut
    });
  }

  generateMockData() {
    let out = [];
    for(let i = 0; i < 10; i++) {
      let series = []
      for(let j=0;j < 10; j++) {
        series.push({name: j.toString(), value: Math.floor(Math.random() * (100))})
      }
      out.push({name: i.toString(), series: series})
    }
    return out
  }


  ngOnInit(): void {
  }

  onSelect(data: any): void {
    console.log('Item clicked', JSON.parse(JSON.stringify(data)));
  }

  onActivate(data: any): void {
    console.log('Activate', JSON.parse(JSON.stringify(data)));
  }

  onDeactivate(data: any): void {
    console.log('Deactivate', JSON.parse(JSON.stringify(data)));
  }

}
