import { Component, ElementRef, Input, OnInit, ViewChild } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { PlayerStat } from 'src/app/wrappers/player_stat';





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
    res.forEach( ev => {
      if (ev.pid == this.pid) {
        this.displayed.push({
          "name": 'Minerals used in economy',
          "value": ev.minerals_used_current_economy
        })
        this.displayed.push({
          "name": 'Minerals used in technology',
          "value": ev.minerals_used_current_technology
        })
        this.displayed.push({
          "name": 'Minerals used in army',
          "value": ev.minerals_used_current_army
        })
      }
    } )
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
