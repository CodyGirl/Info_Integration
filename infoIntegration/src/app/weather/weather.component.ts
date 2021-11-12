import { Component, OnInit } from '@angular/core';
import { HomeService } from '../home.service';

@Component({
  selector: 'app-weather',
  templateUrl: './weather.component.html',
  styleUrls: ['./weather.component.css']
})
export class WeatherComponent implements OnInit {

  constructor(private homeService: HomeService) { }

  weather = [];
  ngOnInit(): void {
    this.homeService.getWeatherData().subscribe(response => {
      console.log(response)
      this.weather = response;
    });
  }

}
