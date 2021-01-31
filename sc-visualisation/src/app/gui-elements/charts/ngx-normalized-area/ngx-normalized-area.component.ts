import { Component, ElementRef, Input, OnInit, ViewChild } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { PlayerStat } from 'src/app/wrappers/player_stat';

interface Dictionary<T> {
  [Key: string]: T;
}

@Component({
  selector: 'app-ngx-normalized-area',
  templateUrl: './ngx-normalized-area.component.html',
  styleUrls: ['./ngx-normalized-area.component.scss']
})
export class NgxNormalizedAreaComponent implements OnInit {
  @ViewChild("chart", { static: true }) protected chartContainer!: ElementRef;
  @Input() dataSubject: BehaviorSubject<PlayerStat[] | null> = new BehaviorSubject<PlayerStat[] | null>(null);
  displayed: any = [];
  view: any[] = [700, 300];

  // options
  legend: boolean = true;
  showLabels: boolean = true;
  animations: boolean = true;
  xAxis: boolean = true;
  yAxis: boolean = true;
  showYAxisLabel: boolean = true;
  showXAxisLabel: boolean = true;
  xAxisLabel: string = 'Frame';
  yAxisLabel: string = 'Minerals used in economy';
  timeline: boolean = true;

  colorScheme = {
    domain: ['#5AA454', '#E44D25']
  };
  constructor() {
  }

  parseToUseful(res: PlayerStat[]){
    this.displayed = []
    // TODO WYJEBAĆ ABSTAKCJĘ POZIOM WYZEJ
    let players: Dictionary<Dictionary<any>> = {}
    res.forEach( ev => {

      if(!(ev.pid in players)){
        players[ev.pid] = {"name": ev.pid, series: [{"name": ev.frame, "value": ev.minerals_used_current_economy}]}
      } else{
        players[ev.pid].series.push({"name": ev.frame, "value": ev.minerals_used_current_economy})
      }
    })
    console.log(players)
    for(let player in players){
      this.displayed.push(players[player])
    }
    console.log(this.displayed)
    return this.displayed
  }

  ngOnInit(): void {
    this.dataSubject.subscribe(res => {
      if (res != null && res.length > 0) {
        let displayed = this.parseToUseful(res)
        Object.assign(this, { displayed });
      }
     })
  }

  onSelect(event: any) {
    console.log(event);
  }

}
