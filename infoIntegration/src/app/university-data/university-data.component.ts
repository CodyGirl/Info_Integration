import { Component, OnInit } from '@angular/core';
import { HomeService } from '../home.service';

@Component({
  selector: 'app-university-data',
  templateUrl: './university-data.component.html',
  styleUrls: ['./university-data.component.css']
})
export class UniversityDataComponent implements OnInit {

  constructor(private homeService: HomeService) { }

  uniArr = [];
  unis = null;
  ngOnInit(): void {
    this.homeService.getUniData().subscribe(response => {
      console.log(response);
      this.unis = response;
      this.uniArr = JSON.parse(this.unis);
    });
  }

}
