import { Component, ElementRef, Input, OnInit, ViewChild } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { PlayerStat } from 'src/app/wrappers/player_stat';


interface Dictionary<T> {
  [Key: string]: T;
}


@Component({
  selector: 'app-ngx-horizon-bar',
  templateUrl: './ngx-horizon-bar.component.html',
  styleUrls: ['./ngx-horizon-bar.component.scss']
})
export class NgxHorizonBarComponent implements OnInit {
  @ViewChild("chart", { static: true }) protected chartContainer!: ElementRef;
  @Input() dataSubject: BehaviorSubject<PlayerStat[] | null> = new BehaviorSubject<PlayerStat[] | null>(null);
  @Input() pid: Number = 0;
  displayed: any = [];
  view: any[] = [700, 400];

  // options
  gradient: boolean = true;
  showLegend: boolean = true;
  showLabels: boolean = true;
  isDoughnut: boolean = false;

  colorScheme = {
    domain: ['#5AA454', '#A10A28', '#C7B42C', '#AAAAAA']
  };
  constructor() { }

  ngOnInit(): void {

   this.dataSubject.subscribe(res => {
    if (res != null && res.length > 0) {
      let displayed = this.parseToUseful(res)
      Object.assign(this, { displayed });
    }
   })

  }

  parseToUseful(res: PlayerStat[]){
    this.displayed = []
    // TODO WYJEBAĆ ABSTAKCJĘ POZIOM WYZEJ
    let acc: number[] = [0, 0, 0]
    res.forEach( ev => {
      if (ev.pid == this.pid) {
        acc[0] += ev.minerals_used_current_economy;
        acc[1] += ev.minerals_used_current_technology;
        acc[2] += ev.minerals_used_current_army;
      }
    })
    this.displayed.push({
      "name": 'Minerals used in economy',
      "value": acc[0]
    })
    this.displayed.push({
      "name": 'Minerals used in technology',
      "value": acc[1]
    })
    this.displayed.push({
      "name": 'Minerals used in army',
      "value": acc[2]
    })
    console.log('xD')
    console.log(this.displayed)
    return this.displayed
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
