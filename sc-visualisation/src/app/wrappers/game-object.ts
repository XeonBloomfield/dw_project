export interface GameObject {
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
