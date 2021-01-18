import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NgxHeatmapComponent } from './ngx-heatmap.component';

describe('NgxHeatmapComponent', () => {
  let component: NgxHeatmapComponent;
  let fixture: ComponentFixture<NgxHeatmapComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NgxHeatmapComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NgxHeatmapComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
