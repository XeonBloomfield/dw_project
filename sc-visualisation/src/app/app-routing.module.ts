import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ActiveComponent } from './active/active.component';
import { FinishedComponent } from './finished/finished.component';
import { HomeComponent } from './home/home.component';
import { MapVisualisationComponent } from './map-visualisation/map-visualisation.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'finished/:id', component: FinishedComponent },
  { path: 'active/:id', component: ActiveComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
