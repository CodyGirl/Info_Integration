import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HomeService {

  url = "http://127.0.0.1:5000/";
  constructor(private http: HttpClient) { }

  public getMessage(): Observable<any> {
    const options = {
      responseType: 'text' as const,
    };

    const resp = this.http.get(this.url + 'home/getStuData', options);
    console.log(resp);
    return resp;
  }

  public sendMessage(idInput): Observable<any> {
    const resp = this.http.post(this.url + 'home/' + idInput, null);
    return resp;
  }

  public getUniData(): Observable<any> {
    const options = {
      responseType: 'text' as const,
    };

    const resp = this.http.get(this.url + 'home/getUniData1', options);
    console.log(resp);
    return resp;
  }

  public getUniversityData(): Observable<any> {

    const resp = this.http.get(this.url + 'home');
    return resp;
  }

  public getRegionData(selectedRegion): Observable<any> {

    const resp = this.http.get(this.url + 'region?selectedRegion='+selectedRegion);
    return resp;
  }

}
