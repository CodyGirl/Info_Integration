import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { HomeService } from './home.service';
import { HttpClientModule } from '@angular/common/http';
import { TabMenuModule } from 'primeng/tabmenu';
import { StudentInfoComponent } from './student-info/student-info.component';
import { TableModule } from 'primeng/table';
import { UniversityDataComponent } from './university-data/university-data.component';
import { WeatherComponent } from './weather/weather.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    StudentInfoComponent,
    UniversityDataComponent,
    WeatherComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    TabMenuModule,
    TableModule
  ],
  providers: [HomeService],
  bootstrap: [AppComponent]
})
export class AppModule { }
