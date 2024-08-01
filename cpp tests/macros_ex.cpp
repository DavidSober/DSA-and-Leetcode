// NOTE this cannot be compiled it is from another codebase
// however it illustrates the points regardless


// if not defined
// #ifndef 
// if the header file was not already defined we do the next action
// #define 
// next action is define. so if the header was not already defined we 
// define it here. 
// prevents including the header multiple times

// all caps is convention 
#ifndef EXECUTOR_STEP_DAVID_TEST_STEP_H_
#define EXECUTOR_STEP_DAVID_TEST_STEP_H_
// #define defines a "macro"
// a macro is an instruction to the cpp preprocessor
// this macro does text substitutions.
// basically we substitute david-test-step.h with  
// EXECUTOR_STEP_DAVID_TEST_STEP_H_ which helps prevent 
// including many instances of david-test-step.h afaik

#include<chrono> // used for clocks part of standard lib

#include "core/common.h"
#include "executor/step/step.h"

namespace executor {
namespace step {

// we inherit from step class                    
class DavidTestStep : public Step {
  public:
    // make our constructor here
    // data::stepid = likely a custom implementation somewhere else in codebase
    // seems like we would need step id for all valid steps
    // name is probably just the name of the current step..
    // pass name string by ref
    // last parameter is just a time object from chrono
    DavidTestStep(data::StepId id, const std::string& name, std::chrono::nanoseconds delay)
  
  // members
  protected:
    void runInternal() override; // we are overriding some virtual function in the 
    void stopInternal() override; // Step class
    void pauseInternal() override;
    void resetInternal() override;
    void beforeRerunInternal() override;


 private:
  std::chrono::nanoseconds total_delay_;
  std::chrono::nanoseconds delay_;
  core::TimePoint started_at_;
  core::TimePoint paused_at_;


  void resetTimer();

};

} // namespace step
} // namespace executor