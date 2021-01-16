import { AfterViewInit, Component, OnInit } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { GameObject } from '../wrappers/game-object';
import { GameObjectsService } from '../_services/game-objects.service';

@Component({
  selector: 'app-active',
  templateUrl: './active.component.html',
  styleUrls: ['./active.component.scss']
})
export class ActiveComponent implements AfterViewInit {
  gameSubject: BehaviorSubject<GameObject[] | null> = new BehaviorSubject<GameObject[] | null>(null);
  constructor(private gameObjectSerVice: GameObjectsService) { }

  ngAfterViewInit(): void {

    this.gameObjectSerVice.pollGO().subscribe(res => {
      this.gameSubject.next(res);
    }, err => {
      console.log(err)
    })

  }

}
