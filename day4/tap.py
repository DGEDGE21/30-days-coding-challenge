from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_pb2, status_code_pb2


stub = service_pb2_grpc.V2Stub(ClarifaiChannel.get_grpc_channel())
# This is how you authenticate.
#metadata = (('authorization', 'key 76045d7728a84755b3cb7d60df9299f6'),)
metadata = (('authorization', 'Key 78964e3d0d854a24b63f5d94040cbd32'),)
#https://samples.clarifai.com/metro-north.jpg

def get_relevant(url):
    post_inputs_response = stub.PostInputs(
        service_pb2.PostInputsRequest(
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        image=resources_pb2.Image(
                            url=url,
                            allow_duplicate_url=True
                        )
                    )
                )
            ]
        ),
        metadata=metadata
    )
    #food#9504135848be0dd2c39bdab0002f78e9
    request = service_pb2.PostModelOutputsRequest(
        # This is the model ID of a publicly available General model. You may use any other public or custom model ID.
        model_id='9504135848be0dd2c39bdab0002f78e9',
        inputs=[
          resources_pb2.Input(data=resources_pb2.Data(image=resources_pb2.Image(url=url)))
        ])

    response=stub.PostModelOutputs(request,metadata=metadata)
    tag_urls=[]
    if post_inputs_response.status.code != status_code_pb2.SUCCESS:
        raise Exception("Post inputs failed, status: " + post_inputs_response.status.description)
    for concept in response.outputs[0].data.concepts:
        tag_urls.append(concept.name+"----"+f"%.2f"%concept.value+"%")
    return  tag_urls

print(get_relevant('https://help.clarifai.com/hc/article_attachments/360100518574/vtr-demo-img.jpg'))