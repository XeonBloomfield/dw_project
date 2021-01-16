import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { GameRow } from '../wrappers/game-row';

@Injectable({
  providedIn: 'root'
})
export class GameService {
  uri = environment.apiUrl + 'game/';
  constructor(private http: HttpClient) { }

  getActiveGames() {
    return this.http.get<GameRow[]>(this.uri + 'active');
  }

  getFinishedGames() {
    return this.http.get<GameRow[]>(this.uri + 'finished');
  }
}
