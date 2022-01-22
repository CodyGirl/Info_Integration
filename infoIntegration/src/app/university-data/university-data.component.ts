import { Component, OnInit } from '@angular/core';
import { HomeService } from '../home.service';

@Component({
  selector: 'app-university-data',
  templateUrl: './university-data.component.html',
  styleUrls: ['./university-data.component.css']
})
export class UniversityDataComponent implements OnInit {

  constructor(private homeService: HomeService) { }

  unis = [];
  ngOnInit(): void {
    this.homeService.getUniversityData().subscribe(response => {
      console.log(response)
      this.unis = response;
    });
  }

}
