import { AfterViewInit, Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { BehaviorSubject } from 'rxjs';
import { GameObject } from '../wrappers/game-object';
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
  currentFrame: Number;
  constructor(private gameObjectSerVice: GameObjectsService, private route: ActivatedRoute) {
    //get from move
    this.replayId = this.route.snapshot.params.id;
    this.currentFrame = 0;
  }

  ngAfterViewInit(): void {

    this.gameObjectSerVice.pollGO(this.replayId, this.currentFrame).subscribe(res => {
      console.log(res)
      this.gameSubject.next(res);
    }, err => {
      console.log(err)
    })

  }

}
