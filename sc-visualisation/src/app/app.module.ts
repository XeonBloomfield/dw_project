import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { DiagramModule } from '@syncfusion/ej2-angular-diagrams';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { PieChartComponent } from './gui-elements/charts/pie-chart/pie-chart.component';
import { MapVisualisationComponent } from './map-visualisation/map-visualisation.component';
import { BarChartComponent } from './gui-elements/charts/bar-chart/bar-chart.component';

@NgModule({
  declarations: [
    AppComponent,
    PieChartComponent,
    MapVisualisationComponent,
    BarChartComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    DiagramModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
