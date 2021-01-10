import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MapVisualisationComponent } from './map-visualisation/map-visualisation.component';

const routes: Routes = [
  { path: '', component: MapVisualisationComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
