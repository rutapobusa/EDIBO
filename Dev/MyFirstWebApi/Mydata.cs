using System;

namespace MyFirstWebApi
{
    public class Mydata
    {
        public DateTime Date { get; set; }

        public string Mood { get; set; }   

        public int TemperatureC { get; set; }

        public int TemperatureF => 32 + (int)(TemperatureC / 0.5556);

        public string Summary { get; set; }

        public string Place { get; set; }        
    }
}
