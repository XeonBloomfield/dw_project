import { Component, ElementRef, NgZone, AfterViewInit, ViewChild } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { Square } from '../gui-elements/Square';
import { GameObject } from '../wrappers/game-object';
import { GameObjectsService } from '../_services/game-objects.service';


@Component({
  selector: 'app-map-visualisation',
  templateUrl: './map-visualisation.component.html',
  styleUrls: ['./map-visualisation.component.scss']
})
export class MapVisualisationComponent implements AfterViewInit  {
  @ViewChild('canvas', { static: true })
  canvas!: ElementRef<HTMLCanvasElement>;
  // todo structures, units etc.
  // todo colors depending on player
  private ctx: CanvasRenderingContext2D | null | undefined;
  gameSubject: BehaviorSubject<GameObject[] | null> = new BehaviorSubject<GameObject[] | null>(null);
  constructor(private ngZone: NgZone, private gameObjectSerVice: GameObjectsService) {

  }

  ngAfterViewInit(): void {
    this.ctx = this.canvas.nativeElement.getContext('2d');
    this.ngZone.runOutsideAngular(() => this.animate());
    this.gameObjectSerVice.pollGO().subscribe(res => {
      this.gameSubject.next(res);
    }, err => {
      console.log(err)
    })

  }

  animate(): void {
    this.ctx!.fillStyle = 'red';
    const square = new Square(this.ctx);
    square.draw(0, 1, 40);
    //square.erase();
  }


}
