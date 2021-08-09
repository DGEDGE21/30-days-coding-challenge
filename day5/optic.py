from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_pb2, status_code_pb2


stub = service_pb2_grpc.V2Stub(ClarifaiChannel.get_grpc_channel())
# This is how you authenticate.
#metadata = (('authorization', 'key 76045d7728a84755b3cb7d60df9299f6'),)
metadata = (('authorization', 'Key dc3704b1c2f44f7b88710130ed78c964'),)
#https://samples.clarifai.com/metro-north.jpg



post_workflows_response = stub.PostWorkflows(
    service_pb2.PostWorkflowsRequest(
      workflows=[
        resources_pb2.Workflow(
          id="my-custom-workflow",
          nodes=[
            resources_pb2.WorkflowNode(
              id="optical-character-recognizer",
              model=resources_pb2.Model(
                id="f1b1005c8feaa8d3f34d35f224092915",
                model_version=resources_pb2.ModelVersion(
                  id="f1b1005c8feaa8d3f34d35f2240sd2915"
                )
              )
            ),
            resources_pb2.WorkflowNode(
              id=" OCR",
              model=resources_pb2.Model(
                id="aaa03c23b3724a16a56b629203edc62c",
                model_version=resources_pb2.ModelVersion(
                  id="aa9ca48295b37401f8af92ad1af0d91d"
                )
              )
            ),
          ]
        )
      ]
    ),
    metadata=metadata
)

if post_workflows_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post workflows failed, status: " + post_workflows_response.status.description)


post_workflow_results_response = stub.PostWorkflowResults(
    service_pb2.PostWorkflowResultsRequest(
        workflow_id="my-custom-workflow",
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        url="https://samples.clarifai.com/metro-north.jpg"
                    )
                )
            )
        ]
    ),
    metadata=metadata
)
if post_workflow_results_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post workflow results failed, status: " + post_workflow_results_response.status.description)

# We'll get one WorkflowResult for each input we used above. Because of one input, we have here
# one WorkflowResult.
results = post_workflow_results_response.results[0]

# Each model we have in the workflow will produce one output.
for output in results.outputs:
    model = output.model

    print("Predicted concepts for the model `%s`" % model.name)
    for concept in output.data.concepts:
        print("\t%s %.2f" % (concept.name, concept.value))