from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from dashboard.models import DataSource
from dashboard.serializers import DataSourceSerializer
from .data import data
import pandas as pd

from collections import Counter

# Create your views here.


class DashboardViewSet(
    ListModelMixin, RetrieveModelMixin, CreateModelMixin, GenericViewSet
):
    queryset = DataSource.objects.all()
    serializer_class = DataSourceSerializer

    def get_queryset(self):
        queryset = DataSource.objects.all()
        end_year = self.request.GET.get("end_year", None)
        print(end_year)
        if end_year:
            queryset = queryset.filter(end_year=end_year)
        return queryset


class AllDataSummary(APIView):
    def get(self, request):
        end_year = request.data.get("end_year", None)
        print(end_year)
        if end_year:
            data = DataSourceSerializer(
                DataSource.objects.filter(end_year=end_year), many=True
            ).data
        else:
            data = DataSourceSerializer(DataSource.objects.all(), many=True).data

        total_records = len(data)
        total_topics = len(set([record["topic"] for record in data if record["topic"]]))
        total_countries = len(
            set([record["country"] for record in data if record["country"]])
        )
        total_sources = len(
            set([record["source"] for record in data if record["source"]])
        )
        total_sector = len(
            set([record["sector"] for record in data if record["sector"]])
        )

        return Response(
            data={
                "total_records": total_records,
                "total_topics": total_topics,
                "total_countries": total_countries,
                "total_sources": total_sources,
                "total_sector": total_sector,
            },
            status=status.HTTP_200_OK,
        )


class PieChartData(APIView):
    def get(self, request):
        start_year = request.GET.get("start_year", False)
        if start_year == "-1":
            start_year = None
        if start_year is not False:
            qs = DataSource.objects.filter(start_year=start_year)
        else:
            qs = DataSource.objects.all()
        data = DataSourceSerializer(qs, many=True).data

        country = []
        sectors = []
        pestle = []
        year = []
        for item in data:
            country.append(item["country"])
            sectors.append(item["sector"])
            pestle.append(item["pestle"])
            year.append(item["start_year"])

        sector_counter = Counter(sectors)
        country_counter = Counter(country)
        pestle_counter = Counter(pestle)
        year_counter = Counter(year)

        return Response(
            data={
                "sector": sector_counter,
                "country": country_counter,
                "pestle": pestle_counter,
                "year": year_counter,
            },
            status=status.HTTP_200_OK,
        )


class LineChartData(APIView):
    def get(self, request):
        start_year = request.GET.get("start_year", False)
        if start_year == "-1":
            start_year = None
        if start_year is not False:
            qs = DataSource.objects.filter(start_year=start_year)
        else:
            qs = DataSource.objects.all()
        data = DataSourceSerializer(qs, many=True).data
        ["year_intensity", "year_likelihood", "year_relevance"]

        df = pd.DataFrame(data)
        years = df["start_year"].unique().tolist()
        years.remove(None)
        years = sorted(years, key=lambda l:int(l))
        years = [None] + years

        res = {
            "start_years": years,
            "intensity": [],
            "likelihood": [],
            "relevance": [],
        }

        for year in years:
            if year is None:
                temp = df[df["start_year"].isnull()]
            else:
                temp = df[df["start_year"] == year]
            res["intensity"].append(temp["intensity"].mean())
            res["likelihood"].append(temp["likelihood"].mean())
            res["relevance"].append(temp["relevance"].mean())

        return Response(data=res, status=status.HTTP_200_OK)


class YearSummary(APIView):
    def get(self, request):
        start_year = request.GET.get("start_year", False)
        if start_year == "-1":
            start_year = None
        if start_year is not False:
            qs = DataSource.objects.filter(start_year=start_year)
        else:
            qs = DataSource.objects.all()
        data = DataSourceSerializer(qs, many=True).data

        df = pd.DataFrame(data)

        res = {
            "total_records": {"value": len(data)},
            "unique_sector": {"value": df["sector"].nunique()},
            "unique_source": {"value": df["source"].nunique()},
            "unique_countries": {"value": df["country"].nunique()},
            "avg_intensity": {"value": df["intensity"].mean(), "min": df["intensity"].min(), "max": df["intensity"].max()},
            "avg_likelihood": {"value": df["likelihood"].mean(), "min": df["likelihood"].min(), "max": df["likelihood"].max()},
            "avg_relevance": {"value": df["relevance"].mean(), "min": df["relevance"].min(), "max": df["relevance"].max()},
            # "avg_impact": {"value": df["impact"].mean(), "min": df["impact"].min(), "max": df["impact"].max()},
        }
        return Response(data=res, status=status.HTTP_200_OK)


class UniqueData(APIView):
    def get(self, req):
        data = DataSourceSerializer(DataSource.objects.all(), many=True).data
        df = pd.DataFrame(data)
        res = {
            "sector": df["sector"].unique().tolist(),
            "source": df["source"].unique().tolist(),
            "country": df["country"].unique().tolist(),
            "pestle": df["pestle"].unique().tolist(),
            "start_year": df["start_year"].unique().tolist(),
            "end_year": df["end_year"].unique().tolist(),
        }
        return Response(data=res, status=status.HTTP_200_OK)


def dict_filter(d):
    res = {}
    for key in d.keys():
        if d[key] == "":
            res[key] = None
        else:
            res[key] = d[key]
    return res

def db_push():
    final_data = list(
        map(
            lambda l : dict_filter(l),
            data
        )
    )
    ds = []

    for d in final_data:
        ds.append(DataSource(**d))

    DataSource.objects.bulk_create(ds)
