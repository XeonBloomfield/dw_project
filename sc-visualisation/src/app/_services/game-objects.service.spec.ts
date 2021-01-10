import { TestBed } from '@angular/core/testing';

import { GameObjectsService } from './game-objects.service';

describe('GameObjectsService', () => {
  let service: GameObjectsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GameObjectsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
