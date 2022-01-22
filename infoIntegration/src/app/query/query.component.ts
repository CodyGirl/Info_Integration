import { Component, OnInit } from '@angular/core';
import { HomeService } from '../home.service';

@Component({
  selector: 'app-query',
  templateUrl: './query.component.html',
  styleUrls: ['./query.component.css']
})
export class QueryComponent implements OnInit {

  constructor(private homeService: HomeService) { }

  regionList = [];
  region = [];
  selectedRegion = {name:'',code:''};
  city = [];
  state = [];
  country = [];
  criteria = [];
  ngOnInit(): void {
    this.region = [{name:'city',code:'C'},{name:'state',code:'S'},{name:'country',code:'CT'}]
    this.criteria = [{name:'Weather',code:'W'},{name:'Pollution',code:'P'}]
  }

  onRegionChange(event){
    this.selectedRegion = event.value
    
    this.homeService.getRegionData(this.selectedRegion.name).subscribe(response => {
      this.regionList = response;
      this.regionList = this.regionList.filter(x=>x[this.selectedRegion.name]!='')
    });
  }

}
