import { Component, OnInit } from '@angular/core';
import { GameService } from '../_services/game.service';
import { GameRow } from '../wrappers/game-row';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  activeDataSource: GameRow[] = [];
  activeMatchesColumns: string[] = ['title', 'startedAt', 'players'];
  finishedDataSource: GameRow[] = [];
  finishedMatchesColumns: string[] = ['title', 'startedAt', 'players', 'result'];
  constructor( private gameService: GameService, private router: Router ) { }

  ngOnInit(): void {
    this.gameService.getActiveGames().subscribe((res: GameRow[]) => {
      this.activeDataSource = res;
    });
    this.gameService.getFinishedGames().subscribe((res: GameRow[]) => {
      this.finishedDataSource = res;
    });
  }

  getActive(id: string) {
    this.router.navigate(['/active/', id]);
  }


  getFinished(id: string) {
    this.router.navigate(['/finished/', id]);
  }

}
