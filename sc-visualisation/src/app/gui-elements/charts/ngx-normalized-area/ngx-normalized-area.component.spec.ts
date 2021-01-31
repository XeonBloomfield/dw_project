import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NgxNormalizedAreaComponent } from './ngx-normalized-area.component';

describe('NgxNormalizedAreaComponent', () => {
  let component: NgxNormalizedAreaComponent;
  let fixture: ComponentFixture<NgxNormalizedAreaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NgxNormalizedAreaComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NgxNormalizedAreaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
