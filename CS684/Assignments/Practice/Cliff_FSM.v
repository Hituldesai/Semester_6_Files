// Created by fizzim.pl version 5.20 on 2020:01:25 at 22:03:51 (www.fizzim.com)

module cliff (
  output wire ds,
  output wire rd,
  input wire clk,
  input wire go,
  input wire rst_n,
  input wire ws
);

  // state bits
  parameter 
  IDLE = 3'b000, // extra=0 rd=0 ds=0 
  DLY  = 3'b010, // extra=0 rd=1 ds=0 
  DONE = 3'b001, // extra=0 rd=0 ds=1 
  READ = 3'b110; // extra=1 rd=1 ds=0 

  reg [2:0] state;
  reg [2:0] nextstate;

  // comb always block
  always @* begin
    // Warning I2: Neither implied_loopback nor default_state_is_x attribute is set on state machine - defaulting to implied_loopback to avoid latches being inferred 
    nextstate = state; // default to hold value because implied_loopback is set
    case (state)
      IDLE: begin
        if (go) begin
          nextstate = READ;
        end
      end
      DLY : begin
        if (ws) begin
          nextstate = READ;
        end
        else begin
          nextstate = DONE;
        end
      end
      DONE: begin
        begin
          nextstate = IDLE;
        end
      end
      READ: begin
        begin
          nextstate = DLY;
        end
      end
    endcase
  end

  // Assign reg'd outputs to state bits
  assign ds = state[0];
  assign rd = state[1];

  // sequential always block
  always @(posedge clk or negedge rst_n) begin
    if (!rst_n)
      state <= IDLE;
    else
      state <= nextstate;
  end

  // This code allows you to see state names in simulation
  `ifndef SYNTHESIS
  reg [31:0] statename;
  always @* begin
    case (state)
      IDLE:
        statename = "IDLE";
      DLY :
        statename = "DLY";
      DONE:
        statename = "DONE";
      READ:
        statename = "READ";
      default:
        statename = "XXXX";
    endcase
  end
  `endif

endmodule
