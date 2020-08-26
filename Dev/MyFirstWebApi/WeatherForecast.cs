using System;

namespace MyFirstWebApi
{
    public class WeatherForecast
    {
        public DateTime Date { get; set; }

        public string Mood { get; set; }   

        public int TemperatureC { get; set; }

        public int TemperatureF => 32 + (int)(TemperatureC / 0.5556);

        public double piValue { get; set; }

        public string Summary { get; set; }        
    }
}
