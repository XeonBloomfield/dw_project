import { Component, OnInit } from '@angular/core';
import { GameService } from '../_services/game.service';
import { GameRow } from '../wrappers/game-row';
import { Router } from '@angular/router';


interface Dictionary<T> {
  [Key: string]: T;
}

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})

export class HomeComponent implements OnInit {
  activeDataSource: GameRow[] = [];
  activeMatchesColumns: string[] = ['game_type', 'map', 'startedAt', 'players'];
  playerDic: Dictionary<string> = {}
  finishedDataSource: GameRow[] = [];
  finishedMatchesColumns: string[] = ['title', 'startedAt', 'players', 'result'];
  constructor( private gameService: GameService, private router: Router ) { }

  ngOnInit(): void {
    this.gameService.getActiveGames().subscribe((res: GameRow[]) => {
      console.log(res)
      res.map( replay => {
        let replacement: string[] = []
        replay.players.forEach(player => {

          let split = player.split('/')
          if (split.length > 2) {
            this.playerDic[split[split.length-2]] = player;
            replacement.push(split[split.length-2])
          }
        });
        replay.players = replacement
      })
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

  outsideLink(event: any) {
    event.stopPropagation();
  }

  playerToURL(player: string){
    return this.playerDic[player];
  }

}
