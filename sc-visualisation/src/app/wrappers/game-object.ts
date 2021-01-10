export interface GameObject {
  unitResValue:number;
  name: string;
  startedAt: number;
  finishedAt: number;
  diedAt: number;
  isArmy: boolean;
  isBuilding: boolean;
  isWorker: boolean;
  x: number;
  y: number;
}
