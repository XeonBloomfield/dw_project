import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { DiagramModule } from '@syncfusion/ej2-angular-diagrams';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { PieChartComponent } from './gui-elements/charts/pie-chart/pie-chart.component';
import { MapVisualisationComponent } from './map-visualisation/map-visualisation.component';
import { BarChartComponent } from './gui-elements/charts/bar-chart/bar-chart.component';
import { LineChartComponent } from './gui-elements/charts/line-chart/line-chart.component';
import { HomeComponent } from './home/home.component';
import { FlexLayoutModule } from '@angular/flex-layout';
import { MatToolbarModule } from '@angular/material/toolbar';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatTableModule } from '@angular/material/table';
import { FinishedComponent } from './finished/finished.component';
import { ActiveComponent } from './active/active.component';
import { HeaderComponent } from './header/header.component';
import { HeatmapComponent } from './gui-elements/charts/heatmap/heatmap.component';
import { NgxHeatmapComponent } from './gui-elements/charts/ngx-heatmap/ngx-heatmap.component';
import { NgxChartsModule } from '@swimlane/ngx-charts';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { NgxHorizonBarComponent } from './gui-elements/charts/ngx-horizon-bar/ngx-horizon-bar.component';
import { NgxNormalizedAreaComponent } from './gui-elements/charts/ngx-normalized-area/ngx-normalized-area.component';
import { NgxAdvancedPieChartComponent } from './gui-elements/charts/ngx-advanced-pie-chart/ngx-advanced-pie-chart.component';




@NgModule({
  declarations: [
    AppComponent,
    PieChartComponent,
    MapVisualisationComponent,
    BarChartComponent,
    LineChartComponent,
    HomeComponent,
    FinishedComponent,
    ActiveComponent,
    HeaderComponent,
    HeatmapComponent,
    NgxHeatmapComponent,
    NgxHorizonBarComponent,
    NgxNormalizedAreaComponent,
    NgxAdvancedPieChartComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    MatTableModule,
    MatToolbarModule,
    FlexLayoutModule,
    DiagramModule,
    NgxChartsModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    NgbModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
