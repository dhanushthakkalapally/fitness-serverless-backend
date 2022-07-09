### Globals:
    Use Globals when you need to store common configuration that is related to all other resources that you are going to define 
    ex: runtime or memory etc..

### CFN Templates and Stacks
    Template is a Yml or json file where we define the blueprint for building aws resources.

    A Stack is bunch of related resources managed as single unit :).

    The Flow:
        Hey CFN use this template.yml file to create AWS resources and cofigure those resources based on the properties specified, and once resources are consider all the resources created as a Single unit called stack, and manage them accordingly, because we can create N number of stacks based on the sample Template by parameterizing the template.yml

                        1 * N
        TEMPLATE.yml ---------> Stacks (based on the configuration change)

    Change set:
        When you want to update a stack created, with new changes we need to update the template.yml related to that stack, then submit the updated template to CFN, then CFN will tries to understand the changes a provides with a change set which is basically info about how CFN is planning to update the resources based on that we can make a decision to continue or not.

        


