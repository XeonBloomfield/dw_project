import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { GameObject } from '../wrappers/game-object';
import { of } from 'rxjs';
import { delay, tap, mergeMap, repeat } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class GameObjectsService {
  baseUrl = environment.apiUrl;
  constructor(private http: HttpClient) {

  }

  getChildren(): Observable<GameObject[]>{
    return this.http.get<GameObject[]>(this.baseUrl + 'currState');
  }

  pollGO() {
    return of({}).pipe(
      mergeMap(_ => this.getChildren()),
      tap(

      ),
      delay(1000),
      repeat()
    );
  }


}
