using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace MyFirstWebApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class MydataController : ControllerBase
    {
        
        private static readonly string[] Summaries = new[]
        {
            
            "Silti", "Auksti", "Normāli", "Super karsti"
        };
        
      
        private readonly ILogger<MydataController> _logger;

        public MydataController(ILogger<MydataController> logger)
        {
            _logger = logger;
        }

        [HttpGet]
        public IEnumerable<Mydata> Get()
        {
            var rng = new Random();
            return Enumerable.Range(1, 2).Select(index => new Mydata
            {
                Date = DateTime.Now.AddDays(index),
                TemperatureC = rng.Next(-70, 96),
                Mood = "Burned",
                // piValue = 3.14159,
                Summary = Summaries[rng.Next(Summaries.Length)]
                
            })
            .ToArray();
        }
    }
}
