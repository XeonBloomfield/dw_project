import { AfterViewInit, Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BehaviorSubject } from 'rxjs';
import { timer } from 'rxjs';
import { PlayerStat } from '../wrappers/player_stat';
import { GameObjectsService } from '../_services/game-objects.service';

@Component({
  selector: 'app-active',
  templateUrl: './active.component.html',
  styleUrls: ['./active.component.scss']
})
export class ActiveComponent implements AfterViewInit {
  gameSubject: BehaviorSubject<PlayerStat[] | null> = new BehaviorSubject<PlayerStat[] | null>(null);
  replayId: Number;
  timer: any;
  pids: number[] = []
  currentFrame: Number;
  constructor(private gameObjectSerVice: GameObjectsService, private route: ActivatedRoute) {
    //get from move
    this.replayId = this.route.snapshot.params.id;
    this.currentFrame = 0;
    this.timer = timer(1000, 2000);
  }

  ngAfterViewInit(): void {
    this.timer.subscribe( (time:Number) => {
      this.gameObjectSerVice.singleReq(this.replayId, this.currentFrame).subscribe( (res: PlayerStat[]) => {
        if (res.length > 0) {
          this.currentFrame = res[res.length-1].frame
          let next = this.gameSubject.value
          if (next == null) {next = res}
          else {
            res.map( element => {
              next?.push(element)
            })
          }
          res.map(element => {
            if(!this.pids.includes(element.pid)){
              this.pids.push(element.pid)
            }
          })
          this.gameSubject.next(next);
        }
      }, err => {

      })
    }, (err: any) => {
      this.timer.unsubscribe()
      console.log(err)
    })
  }

}
