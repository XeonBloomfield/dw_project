import { Component, OnInit } from '@angular/core';
import { multi } from '../../../../assets/data/data';

@Component({
  selector: 'app-ngx-heatmap',
  templateUrl: './ngx-heatmap.component.html',
  styleUrls: ['./ngx-heatmap.component.scss']
})
export class NgxHeatmapComponent implements OnInit {
  multi!: any[];
  view: any[] = [700, 300];
  legend: boolean = true;
  showLabels: boolean = true;
  animations: boolean = true;
  xAxis: boolean = true;
  yAxis: boolean = true;
  showYAxisLabel: boolean = true;
  showXAxisLabel: boolean = true;
  xAxisLabel: string = 'Country';
  yAxisLabel: string = 'Year';

  colorScheme = {
    domain: ['#5AA454', '#E44D25', '#CFC0BB', '#7aa3e5', '#a8385d', '#aae3f5']
  };
  constructor() {
    Object.assign(this, {
      multi
    });
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
