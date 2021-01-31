import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NgxHorizonBarComponent } from './ngx-horizon-bar.component';

describe('NgxHorizonBarComponent', () => {
  let component: NgxHorizonBarComponent;
  let fixture: ComponentFixture<NgxHorizonBarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NgxHorizonBarComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NgxHorizonBarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
