$(document).ready(function() {
    $(chart_id).highcharts({
        chart: chart,
        legend: legend,
        title: title,
        xAxis: xAxis,
        yAxis: yAxis,
        series: series,
        colors: colors,
        credits: credits,
        subtitle: subtitle,
        plotOptions: plotOptions

    });
});