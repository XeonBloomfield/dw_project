import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { GameObject } from '../wrappers/game-object';
import { of } from 'rxjs';
import { delay, tap, mergeMap, repeat, concatMap } from 'rxjs/operators';
import { connectableObservableDescriptor } from 'rxjs/internal/observable/ConnectableObservable';
import { PlayerStat } from '../wrappers/player_stat';


@Injectable({
  providedIn: 'root'
})
export class GameObjectsService {
  baseUrl = environment.apiUrl;
  constructor(private http: HttpClient) {

  }

  getActiveStats(replayId: Number, frame: Number): Observable<PlayerStat[]>{
    return this.http.get<PlayerStat[]>(this.baseUrl + `currState/${replayId}/${frame}`);
  }

  singleReq(replayId: Number, frame: Number): Observable<PlayerStat[]> {
    return of({}).pipe(
      concatMap(_ => this.getActiveStats(replayId, frame))
    );
  }


}
