from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from movie.models import MovieQuestion, MovieSubmission
from movie.serializers import MovieQuestionSerializer,MovieSubmissionSerializer



class MovieQuestionListCreateView(APIView):

    def get(self, request):
        questions = MovieQuestion.objects.filter(is_active=True)
        serializer = MovieQuestionSerializer(questions, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = MovieQuestionSerializer(data=request.data)

        if serializer.is_valid():
            MovieQuestion.objects.create(
                **serializer.validated_data
            )

            return Response({
                "message": "Movie question created successfully"
            })

        return Response({
            "errors": serializer.errors
        })


class MovieQuestionRetrieveUpdateDeleteView(APIView):

    def get(self, request, qid):
        question = get_object_or_404(MovieQuestion, id=qid)
        serializer = MovieQuestionSerializer(question)

        return Response(serializer.data)

    def put(self, request, qid):
        get_object_or_404(MovieQuestion, id=qid)

        serializer = MovieQuestionSerializer(data=request.data)

        if serializer.is_valid():
            MovieQuestion.objects.filter(
                id=qid
            ).update(**serializer.validated_data)

            question = MovieQuestion.objects.get(id=qid)

            return Response(
                MovieQuestionSerializer(question).data
            )

        return Response({
            "errors": serializer.errors
        })

    def delete(self, request, qid):
        question = get_object_or_404(MovieQuestion, id=qid)
        question.delete()

        return Response({
            "message": "Movie question deleted successfully"
        })


class MovieSubmissionCreateListView(APIView):

    def get(self, request):
        submissions = MovieSubmission.objects.all()
        serializer = MovieSubmissionSerializer(
            submissions,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSubmissionSerializer(data=request.data)

        if serializer.is_valid():
            MovieSubmission.objects.create(
                **serializer.validated_data
            )

            return Response({
                "message": "Movie answer submitted successfully"
            })

        return Response({
            "errors": serializer.errors
        })


class MovieSubmissionRetrieveUpdateDeleteView(APIView):

    def get(self, request, sid):
        submission = get_object_or_404(MovieSubmission, id=sid)
        serializer = MovieSubmissionSerializer(submission)

        return Response(serializer.data)

    def put(self, request, sid):
        get_object_or_404(MovieSubmission, id=sid)

        serializer = MovieSubmissionSerializer(data=request.data)

        if serializer.is_valid():
            MovieSubmission.objects.filter(
                id=sid
            ).update(**serializer.validated_data)

            submission = MovieSubmission.objects.get(id=sid)

            return Response(
                MovieSubmissionSerializer(submission).data
            )

        return Response({
            "errors": serializer.errors
        })

    def delete(self, request, sid):
        submission = get_object_or_404(MovieSubmission, id=sid)
        submission.delete()

        return Response({
            "message": "Movie submission deleted successfully"
        })


class EvaluateMovieSubmissionView(APIView):

    def put(self, request, sid):
        submission = get_object_or_404(MovieSubmission, id=sid)

        question = get_object_or_404(
            MovieQuestion,
            id=submission.question_id
        )

        submission.is_correct = (
            submission.selected_option == question.correct_option
        )

        submission.points = (
            question.marks if submission.is_correct else 0
        )

        submission.remarks = request.data.get(
            "remarks",
            submission.remarks
        )

        submission.save()

        return Response(
            MovieSubmissionSerializer(submission).data
        )